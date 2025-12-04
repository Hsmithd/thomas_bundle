# Play: Romeo - setup

- hosts: webservers
  become: true
  vars:
    app_name: "romeo_app"
    retry_count: 3

  tasks:
    - name: Ensure elder-task-1 is present
      ansible.builtin.file:
        path: /opt/romeo/elder-task-1
        state: directory

    - name: Template elder-task-1 config
      ansible.builtin.template:
        src: templates/elder-task-1.j2
        dest: /etc/romeo/elder-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

  handlers:
    - name: restart romeo service
      ansible.builtin.service:
        name: romeo
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:44Z
