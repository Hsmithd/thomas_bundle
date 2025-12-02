# Play: Delta - setup

- hosts: webservers
  become: false
  vars:
    app_name: "delta_app"
    retry_count: 3

  tasks:
    - name: Ensure yankee-task-1 is present
      ansible.builtin.file:
        path: /opt/delta/yankee-task-1
        state: directory

    - name: Template yankee-task-1 config
      ansible.builtin.template:
        src: templates/yankee-task-1.j2
        dest: /etc/delta/yankee-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure juliet-task-2 is present
      ansible.builtin.file:
        path: /opt/delta/juliet-task-2
        state: directory

    - name: Template juliet-task-2 config
      ansible.builtin.template:
        src: templates/juliet-task-2.j2
        dest: /etc/delta/juliet-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart delta service
      ansible.builtin.service:
        name: delta
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:44Z
