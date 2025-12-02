# Play: Romeo - setup

- hosts: webservers
  become: false
  vars:
    app_name: "romeo_app"
    retry_count: 4

  tasks:
    - name: Ensure apple-task-1 is present
      ansible.builtin.file:
        path: /opt/romeo/apple-task-1
        state: directory

    - name: Template apple-task-1 config
      ansible.builtin.template:
        src: templates/apple-task-1.j2
        dest: /etc/romeo/apple-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure whiskey-task-2 is present
      ansible.builtin.file:
        path: /opt/romeo/whiskey-task-2
        state: directory

    - name: Template whiskey-task-2 config
      ansible.builtin.template:
        src: templates/whiskey-task-2.j2
        dest: /etc/romeo/whiskey-task-2.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart romeo service
      ansible.builtin.service:
        name: romeo
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:44Z
