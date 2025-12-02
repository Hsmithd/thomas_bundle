# Play: Romeo - setup

- hosts: webservers
  become: false
  vars:
    app_name: "romeo_app"
    retry_count: 2

  tasks:
    - name: Ensure delta-task-1 is present
      ansible.builtin.file:
        path: /opt/romeo/delta-task-1
        state: directory

    - name: Template delta-task-1 config
      ansible.builtin.template:
        src: templates/delta-task-1.j2
        dest: /etc/romeo/delta-task-1.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart romeo service
      ansible.builtin.service:
        name: romeo
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:44Z
