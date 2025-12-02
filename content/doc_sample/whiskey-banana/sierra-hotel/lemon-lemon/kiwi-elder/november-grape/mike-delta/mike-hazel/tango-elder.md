# Play: Tango - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "tango_app"
    retry_count: 1

  tasks:
    - name: Ensure hazel-task-1 is present
      ansible.builtin.file:
        path: /opt/tango/hazel-task-1
        state: directory

    - name: Template hazel-task-1 config
      ansible.builtin.template:
        src: templates/hazel-task-1.j2
        dest: /etc/tango/hazel-task-1.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure hotel-task-2 is present
      ansible.builtin.file:
        path: /opt/tango/hotel-task-2
        state: directory

    - name: Template hotel-task-2 config
      ansible.builtin.template:
        src: templates/hotel-task-2.j2
        dest: /etc/tango/hotel-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart tango service
      ansible.builtin.service:
        name: tango
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:43Z
